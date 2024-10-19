Require Import Coq.Arith.Arith.

Inductive expr :=
    | Const (n : nat)
    | Plus (e1 e2 : expr)
    | Times (e1 e2 : expr).

Fixpoint eval_expr (e : expr) : nat :=
    match e with
    | Const n => n
    | Plus e1 e2 => eval_expr e1 + eval_expr e2
    | Times e1 e2 => eval_expr e1 * eval_expr e2
    end.

Fixpoint flip (e: expr) : expr :=
    match e with
    | Const n => Const n
    | Plus e1 e2 => Plus (flip e2) (flip e1)
    | Times e1 e2 => Times (flip e2) (flip e1)
    end.

Lemma flip_preserves_semantics:
    forall e, eval_expr e = eval_expr (flip e).
Proof.
    induction e.
    * simpl; reflexivity.
    * simpl; rewrite IHe1; rewrite IHe2; apply Nat.add_comm.
    * simpl; rewrite IHe1; rewrite IHe2; apply Nat.mul_comm.
Qed.

Require Import List.
Import ListNotations.
Print list.
Check list.
Check list nat.
Check list bool.

Fixpoint sum (l: list nat) : nat :=
    match l with
    | nil => 0
    | cons n l' => n + sum l'
    end.

Compute sum [1; 2; 3].

Fixpoint sum_tailrec' (l: list nat) (acc: nat) : nat :=
    match l with
    | nil => acc
    | cons n l' => sum_tailrec' l' (n + acc)
    end.
Definition sum_tailrec (l: list nat) := sum_tailrec' l 0.

Compute sum_tailrec [1; 2; 3].

Theorem sum_sum_tailrec:
    forall l, sum l = sum_tailrec l.
Proof.
    induction l.
    - simpl. unfold sum_tailrec. simpl. reflexivity. (* auto.*)
    - simpl. unfold sum_tailrec. simpl.
      unfold sum_tailrec in IHl.
Abort.

Require Import Lia.

Lemma sum_sum_tailrec':
    forall l acc, acc + sum l = sum_tailrec' l acc.
Proof.
    induction l.
    - intro. simpl. apply Nat.add_0_r.
    - intro acc'. simpl. rewrite <- IHl.
      lia.
Qed.

Theorem sum_sum_tailrec:
    forall l, sum l = sum_tailrec l.
Proof.
    intro.
    (* apply sum_sum_tailrec' with (acc := 0). *)
    unfold sum_tailrec.
    rewrite <- Nat.add_0_l with (n := sum l).    
    apply sum_sum_tailrec'.
Qed.

Inductive instr :=
| Push (n : nat)
| Add
| Multiply.

Definition prog := list instr.

Definition stack := list nat.

Definition eval_instr (i: instr) (s: stack) : stack :=
    match i with
    | Push n => n :: s
    | Add => match s with
        | a :: b :: s' => (a + b) :: s'
        | _ => s
        end
    | Multiply => match s with
        | a :: b :: s' => (a * b) :: s'
        | _ => s
        end
    end.

Fixpoint eval_prog' (p: prog) (s: stack) : stack :=
    match p with
    | nil => s
    | cons i p' => eval_prog' p' (eval_instr i s)
    end.

Definition eval_prog (p: prog) : stack := 
    eval_prog' p nil.

Compute eval_prog [Push 1; Push 2; Add].

Fixpoint compile (e: expr) : prog :=
    match e with
    | Const n => [Push n]
    | Plus e1 e2 => compile e2 ++ compile e1 ++ [Add]
    | Times e1 e2 => compile e2 ++ compile e1 ++ [Multiply]
    end.

Compute eval_prog (compile (Plus (Const 1) (Const 2))).

Theorem compile_correct:
    forall e, cons (eval_expr e) nil = eval_prog (compile e).
Proof.
    induction e.
    - auto.
    - simpl. unfold eval_prog in *. 
Abort.

Lemma compile_correct':
    forall e p, eval_prog (compile e ++ p) = eval_prog' p [(eval_expr e)].
Proof.
    induction e; auto.
    - intro. simpl.
      rewrite <- app_assoc.
      rewrite IHe2.
      rewrite <- app_assoc.
      unfold eval_prog in IHe2.
      Abort.
    
Lemma compile_correct':
    forall e p s, eval_prog' (compile e ++ p) s = eval_prog' p ((eval_expr e) :: s).
Proof.
    induction e; auto.
    - intros.
      simpl.
      rewrite <- app_assoc.
      rewrite IHe2.
      rewrite <- app_assoc.
      rewrite IHe1.
      simpl.
      reflexivity.
    - intros.
      simpl.
      rewrite <- app_assoc.
      rewrite IHe2.
      rewrite <- app_assoc.
      rewrite IHe1.
      simpl.
      reflexivity.
Qed.

Theorem compile_correct:
    forall e, cons (eval_expr e) nil = eval_prog (compile e).
Proof.
    intro.
    unfold eval_prog.
    rewrite <- app_nil_r with (l := compile e).
    rewrite -> compile_correct'.
    simpl. reflexivity.
Qed.
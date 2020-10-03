from postgres:12-alpine
ENV POSTGRES_USER=utctf_root
ENV POSTGRES_PASSWORD=thisisthelongestpasswordforroot1111
ENV POSTGRES_DB=utctf_db
ENV PROBLEM_DB_USER=utctf_prob1
ENV PROBLEM_DB_PASSWORD=thisisthenonrootpasswordforutctf1

ADD ./init /docker-entrypoint-initdb.d/

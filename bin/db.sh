if [ $# -ne 1 ]; then
  exit 1
fi

case $1 in
  "create")
    if [ -f var/WorkoutBuddies.sqlite3 ]; then
        rm -rf var/WorkoutBuddies.sqlite3
    fi
    mkdir -p var
    sqlite3 var/WorkoutBuddies.sqlite3 < sql/schema.sql
    sqlite3 var/WorkoutBuddies.sqlite3 < sql/data.sql
    ;;

  "destroy")
    rm -rf var/WorkoutBuddies.sqlite3
    ;;

  "reset")
    rm -rf var/WorkoutBuddies.sqlite3 var
    mkdir -p var
    sqlite3 var/WorkoutBuddies.sqlite3 < sql/schema.sql
    sqlite3 var/WorkoutBuddies.sqlite3 < sql/data.sql
    ;;
esac
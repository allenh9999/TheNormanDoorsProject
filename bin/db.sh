if [ -f var/WorkoutBuddies.sqlite3 ]; then
   rm -rf var/WorkoutBuddies.sqlite3
fi
mkdir -p var
sqlite3 var/WorkoutBuddies.sqlite3 < sql/schema.sql
sqlite3 var/WorkoutBuddies.sqlite3 < sql/data.sql
servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    echo "configure_monitoring_agent" "$server"
done
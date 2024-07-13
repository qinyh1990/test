#!/usr/bin/expect

# 定义日志文件的路径

# 检查是否有运行中的 Docker 容器
set running_containers [exec docker ps -q]

if {$running_containers eq ""} {
    puts "No running containers. Starting script..."

    # 设置日志和超时时间
    set timeout 120

    # 执行 /root/io.sh 并处理交互
    spawn /root/io.sh
    expect {
        "Do you want to continue? (Yes/no):" {
            send "yes\r"
            exp_continue
        }
        timeout {
            puts "Timeout waiting for prompt"
            exit 1
        }
        eof {
            puts "End of script"
        }
    }
} else {
    puts "There are running containers."
}

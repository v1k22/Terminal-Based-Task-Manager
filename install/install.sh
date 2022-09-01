echo '----------Installing--------------'

mkdir -p /etc/bd

tee -a /root/.bashrc << EOF
# text inserted by TM - Task Manager program
display_date(){
        tm --summary
}
PS1='\${debian_chroot:+(\$debian_chroot)}\u@\h:\w\\$ \n [\$(display_date)] 🦁 '
# END of text insert by TM
EOF

echo 'Copying executables to /usr/bin'
cp ../dist/* /usr/bin/tm

echo '\n\n'
echo 'Run source ~/.bashrc to apply changes'

source /root/.bashrc

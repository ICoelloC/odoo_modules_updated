echo "<odoo><data>"

while read line
do
    nombre=$(echo $line | cut -d',' -f1)
    start_date=$(echo $line | cut -d',' -f2)
    end_date=$(echo $line | cut -d',' -f3)
    presential=$(echo $line | cut -d',' -f4)
    echo "<record id='event$name' model='dev_meet.event'>"
    echo "<field name='name'>$nombre</field>"
    echo "<field name='start_date'>$start_date</field>"
    echo "<field name='end_date'>$end_date</field>"
    echo "<field name='presential'>$presential</field>"
    echo "</record>"
done

echo "</data></odoo>"

echo "<odoo><data>"

while read line
do
    nombre=$(echo $line | cut -d',' -f1)
    inicio=$(echo $line | cut -d',' -f2)
    fin=$(echo $line | cut -d',' -f3)
    presencial=$(echo $line | cut -d',' -f4)
    echo "<record id='event$nombre' model='dev_meet.event'>"
    echo "<field name='name'>$nombre</field>"
    echo "<field name='start_date'>$inicio</field>"
    echo "<field name='end_date'>$fin</field>"
    echo "<field name='presential'>$presencial</field>"
    echo "</record>"
done

echo "</data></odoo>"

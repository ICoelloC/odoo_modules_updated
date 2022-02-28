echo "<odoo><data>"

while read line
do
    nombre=$(echo $line | cut -d',' -f1)
    apellidos=$(echo $line | cut -d',' -f2)
    dni=$(echo $line | cut -d',' -f3)
    mail=$(echo $line | cut -d',' -f4)
    phone=$(echo $line | cut -d',' -f5)
    cat=$(echo $line | cut -d',' -f6)
    echo "<record id='developer$dni' model='dev_meet.developer'>"
    echo "<field name='name'>$nombre</field>"
    echo "<field name='nickname'>$apellidos</field>"
    echo "<field name='dni'>$dni</field>"
    echo "<field name='email'>$mail</field>"
    echo "<field name='phone'>$phone</field>"
    echo "<field name='category'>$cat</field>"
    echo "<field name='photo'>$(base64 dev.jpg)</field>"
    echo "</record>"
done

echo "</data></odoo>"
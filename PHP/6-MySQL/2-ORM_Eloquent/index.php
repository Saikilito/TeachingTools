<?php 
error_reporting(E_ALL);
ini_set('display_errors', '1');

use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Database\Eloquent\Model ;

class Job extends Model {

    protected $table ='jobs';

    public function getDurationAsString(){
        $years = floor($this->months / 12);
        $extraMonths = $this->months % 12 ;

        return "Job duration: $years years $extraMonths months";
    }
}

$capsule = new Capsule;

$capsule->addConnection([
    'driver'    => 'mysql',
    'host'      => 'localhost',
    'database'  => 'database_test',
    'username'  => 'root',
    'password'  => 'root',
    'charset'   => 'utf8',
    'collation' => 'utf8_unicode_ci',
    'prefix'    => '',
]);


// Make this Capsule instance available globally via static methods... (optional)
$capsule->setAsGlobal();
// Setup the Eloquent ORM... (optional; unless you've used setEventDispatcher())
$capsule->bootEloquent();

if(!empty($_POST))
{
    $job = new Job();
    $job->title = $_POST['title'];
    $job->description = $_POST['description'];
    $job->visible = true ;
    $job->save();
}

require('addJob.php');
?>
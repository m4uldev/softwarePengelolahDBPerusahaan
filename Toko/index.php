<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dataperusahaan";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Initialize search query
$searchQuery = "";

// Check if search form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['cari'])) {
  $searchQuery = $_POST['cari'];
  $sql = "SELECT * FROM `db_produk` WHERE namaBarang LIKE '%$searchQuery%'";
} else {
  $sql = "SELECT * FROM `db_produk`";
}
$jumlahData = '';
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toko Maulid</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            font-family: Arial;
            align-items: center;
            margin: 0;
            background-color: #f0f0f0;
        }
        h1 {
            margin-bottom: 20px;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(2, 1fr);
            gap: 10px;
            width: 60%;
            max-width: 800px;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .box {
            justify-content: center;
            align-items: center;
            border: 1px solid #ccc;
            padding: 20px;
            font-size: 1.2em;
            background-color: #e0e0e0;
        }
        input[type="text"] {
            width: 300px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px 0 0 4px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            border: none;
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            border-radius: 0 4px 4px 0;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Toko Maulid</h1>
    <div style="display: flex; padding: 15px;">
      <form action="" method="post">
        <input type="text" name="cari" placeholder="Cari nama barang" value="<?php echo htmlspecialchars($searchQuery); ?>">
        <button type="submit" name="tom" class="cari_barang">Cari</button>
      </form>
    </div>
    <div class="container">
        <?php 
        if ($result->num_rows > 0) {
          $jumlahData = 0;
          while($row = $result->fetch_assoc()) {
            echo "
              <div class='box'>
                <h4>{$row['namaBarang']}</h4>
                <p>Harga : Rp.{$row['hargaBarang']}</p>
                <p>Stok : {$row['stokBarang']}</p>
                <p>Deskripsi : {$row['deskripsiBarang']}</p>
                <button>Beli</button>
              </div>
            ";
            $jumlahData++;
          }
        } else {
          echo "<p style='color: red;'>Hasil pencarian $searchQuery tidak ditemukan !</p>";
        }
        ?>
    </div>
    <?php 
      echo "<p style='color: green;'>Jumlah $jumlahData data pada pencarian $searchQuery</p>";
    ?>
</body>
</html>

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

Website: [https://uptick.network](https://uptick.network)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (29)
```
peers="f296bfda3c0c3f46059c89d3ee02f3f11d95d00b@162.55.234.70:55056,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,79888e0547bfb9937e4a6f4fbdca7ccbf46cbbde@155.133.23.88:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,0fcdc6af694d5b9995340549e5ce444dc96de3e0@195.201.197.4:15656,40e340692ead998ad22d4c5907d4ca27ac1cdbc8@65.109.34.9:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,962e467376dd18f68bbab10cda5a336a1a08aa4b@65.21.134.202:26666,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,12fe5ed38770b4bb59c59e183ec1161aebda2a4e@185.173.38.18:26656,2d892493335b4bb1582dabcaa1e832bcba041e79@95.217.4.62:26656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,8340a33a3794dfef56159f412012c16ce51d96dc@65.109.85.52:46656,7175172406a124862dc545b8fb1e3545c35173f9@176.9.146.72:14656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```

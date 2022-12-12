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

**live-peers** (25)
```
peers="0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,96a2fd192db329ff9df3f44569f0fe452ea9f19e@65.108.232.110:15656,8340a33a3794dfef56159f412012c16ce51d96dc@65.109.85.52:46656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,12fe5ed38770b4bb59c59e183ec1161aebda2a4e@185.173.38.18:26656,79888e0547bfb9937e4a6f4fbdca7ccbf46cbbde@155.133.23.88:26656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,40e340692ead998ad22d4c5907d4ca27ac1cdbc8@65.109.34.9:60856,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,07df6fd3f41c4bda761931831439ab248eb3dae4@91.223.3.190:55056,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```

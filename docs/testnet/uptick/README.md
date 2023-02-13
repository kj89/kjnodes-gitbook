# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)




## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: [https://uptick-testnet.grpc.kjnodes.com](https://uptick-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (26)
```bash
peers="b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,75f90b4070eab7a20dc60974c85069389c77d89d@38.242.239.27:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,8096fef589ead4cd3a1aef83110b0241e63d5747@38.242.239.25:26656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,50e92c60d1b8c6681044778d74caaeef51a26ddd@94.130.207.215:15656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,07df6fd3f41c4bda761931831439ab248eb3dae4@91.223.3.190:55056,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```

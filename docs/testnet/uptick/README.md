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

**live-peers** (21)
```bash
peers="1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,75f90b4070eab7a20dc60974c85069389c77d89d@38.242.239.27:26656,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,8096fef589ead4cd3a1aef83110b0241e63d5747@38.242.239.25:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,07df6fd3f41c4bda761931831439ab248eb3dae4@91.223.3.190:55056,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```

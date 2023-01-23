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

**live-peers** (23)
```bash
peers="0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,7175172406a124862dc545b8fb1e3545c35173f9@176.9.146.72:14656,453aff3405698476967251ee253a03bedf4f0dce@178.211.139.124:15656,821cec653e1bdcd6e0ea7db62ddc65e7dae9fc5b@190.2.136.58:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,07df6fd3f41c4bda761931831439ab248eb3dae4@91.223.3.190:55056,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```

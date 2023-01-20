# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


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

**live-peers** (19)
```bash
peers="1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,f296bfda3c0c3f46059c89d3ee02f3f11d95d00b@162.55.234.70:55056,0fcdc6af694d5b9995340549e5ce444dc96de3e0@195.201.197.4:15656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```

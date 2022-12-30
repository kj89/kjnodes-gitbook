# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


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

**live-peers** (14)
```
peers="0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```

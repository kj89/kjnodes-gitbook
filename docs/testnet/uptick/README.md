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
peers="0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,453aff3405698476967251ee253a03bedf4f0dce@178.211.139.124:15656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,7175172406a124862dc545b8fb1e3545c35173f9@176.9.146.72:14656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,20aaf646f9c766a8b81d838554ba6e593122ed1f@46.4.122.236:36656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```

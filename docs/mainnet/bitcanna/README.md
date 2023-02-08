# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: [https://bitcanna.grpc.kjnodes.com](https://bitcanna.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```bash
peers="803fc66e3bd7b724921ef9c40636067f36e880c6@65.108.199.222:26356,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```

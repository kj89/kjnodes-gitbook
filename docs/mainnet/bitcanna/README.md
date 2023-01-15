# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


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
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,9065a2ebd940ad44e2955361fe27809b9f6e2765@159.148.31.234:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```

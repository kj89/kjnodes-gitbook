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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,cb0848b84987c37ba0fa465585c6b9d6cec6deab@65.108.77.98:26696,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```

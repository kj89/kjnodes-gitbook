# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

Website: [https://www.bitcanna.io](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


## Public endpoints

* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,577e5457c1e1fc8e0958432e902ad8c86cef2336@169.155.168.54:26656,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,36a17684dc4809eb0c722aa4b5bd829b0429e8a1@207.246.84.132:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


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
peers="d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,9301659e822226a1eaefe6e6fa99da96c99d7db6@94.130.10.43:30656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```

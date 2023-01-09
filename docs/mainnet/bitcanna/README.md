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
peers="17de6cb601246b429027545e420df0a60fe3591e@65.21.200.224:13056,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```

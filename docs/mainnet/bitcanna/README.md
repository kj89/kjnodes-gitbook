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
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```

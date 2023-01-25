# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="eae08499096faf872ec686c0b5d66a7ad5ad510b@159.223.69.75:20656,8211450a8c7f31b5b3a1f3b792354de5fed1d792@85.10.198.169:33656,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,e17a62b746f6dc3a19a49887ba484306859c4beb@206.246.71.251:45656,b55529476327676f398ce40320bae8eb28c5d4fe@46.101.81.60:26656,0847771f2b70e14a99e39411b96d748c068fadf9@141.95.65.26:29556,8f50c04195cc82d0da34e33cfeb0daa694b14479@65.108.105.48:18556,005d02c48d411f0564bb285b5e8253609dd29cf2@65.109.82.106:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```

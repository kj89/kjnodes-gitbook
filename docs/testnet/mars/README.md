# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


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
peers="140249a417f4fc3e0c94726bbb4a58d2beaf3ebc@65.108.75.107:29656,4aae6c505e4a20415b0d3680e75a526d48c6a370@65.108.238.217:11254,c84154bb4aba1cd78169ac2b30d34ee8a1966c6e@194.163.179.175:16656,79b82583f2d8a0ed187fa2edf1f06c0c712d4989@185.48.24.106:28656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,ef0736768c2f351c597c7307957a36de40209ef3@5.161.114.1:26656,92c3c938d39362d743c3d621619642fc81d5eb0e@91.230.110.200:45656,aea09eb8f366e388ca74e3f3ffe6909d5c89d1b9@95.214.55.155:22656,b9b382cf6b890a534f1e94a7e9174ed19e39a80e@95.217.189.43:24656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```

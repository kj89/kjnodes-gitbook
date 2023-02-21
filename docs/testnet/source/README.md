# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: [https://source-testnet.grpc.kjnodes.com](https://source-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="9260303a16969bbf4360b462d80ce12f77c4d3a1@43.131.35.28:26656,eced2139ee25834946b40a30a9469f247c9060a0@62.171.178.219:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,2c20351736d27e50952695801a4d77122ead307f@62.171.180.83:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

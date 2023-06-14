# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,db0264c412618949ce3a63cb07328d027e433372@146.19.24.101:26646,801c31f8571c222764e742bd2fda625d40afe503@65.21.225.178:26666,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,013e00c359cdd97d548910bdf9f027564fd75cb8@65.108.73.124:23656,1bffcd1690806b5796415ff72f02157ce048bcdd@144.76.67.53:2580"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```

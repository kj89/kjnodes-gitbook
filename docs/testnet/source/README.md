# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (12)
```bash
peers="1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,e2d9b74c65a383a34f9156adb47583e67f996a66@65.109.90.171:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,805c327443d9a2b425d16a402c23cb9cbfa36388@178.18.243.46:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,86216a2e88322ca534fedaa91898272cc11d3cc9@173.249.23.196:28656,854048fcfb453297742b76cc5c6b7555eeb25110@213.239.207.175:31656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

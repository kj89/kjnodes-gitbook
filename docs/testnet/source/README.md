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

**live-peers** (10)
```bash
peers="291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,c4a25dde02d45af2d9f90e10d136c5d399183730@38.242.137.186:28656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,86216a2e88322ca534fedaa91898272cc11d3cc9@173.249.23.196:28656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

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
peers="da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,c4a25dde02d45af2d9f90e10d136c5d399183730@38.242.137.186:28656,854048fcfb453297742b76cc5c6b7555eeb25110@213.239.207.175:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

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
peers="291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,1709ae02a391357bad468987e208075ef53f969b@3.135.249.173:26656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,636c7206a1a9a817768766a1f243d27398159028@144.76.97.251:36656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

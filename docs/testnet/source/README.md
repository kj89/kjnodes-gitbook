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

**live-peers** (11)
```bash
peers="1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

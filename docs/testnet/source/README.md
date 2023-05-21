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
peers="1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,c4a25dde02d45af2d9f90e10d136c5d399183730@38.242.137.186:28656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```

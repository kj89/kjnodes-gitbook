# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.3.0 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:14390

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:14356
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:14359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,fb94493b7744f7bcde0f9eb3e1657a137264cde4@95.216.171.110:26656,0a7ece014d1dbffe5bc0b7a9f5399573ac8a335d@144.91.92.219:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,3a0ca1d94b199af43ae28d32572dda8c5cc723d0@15.235.114.158:26656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,c6e62e0d9998413692ce1aefd05ae5eeb699a691@65.109.122.105:60756,e367dd3cbfca4b6d78271ed5585c469d9f1cb4b4@51.89.6.150:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

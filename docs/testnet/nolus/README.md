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

**live-peers** (11)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,5ded92727197e59aa382180628710744910d932b@174.138.23.52:20756,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

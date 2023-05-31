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
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,5ded92727197e59aa382180628710744910d932b@174.138.23.52:20756,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6d76e4e0f73efa4e693b9d32934b09a025c6aa62@38.242.128.166:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,18163407ab3a5045cd094f8e546e2732fcd53d32@45.8.132.82:26656,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

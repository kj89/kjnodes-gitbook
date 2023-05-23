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
peers="17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,077b4aea6477cbd7023ba861415c9e9f7e8a8a30@185.246.86.152:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

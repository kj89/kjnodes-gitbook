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
peers="17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,7f5ce546e0ffec994995198e0a1b87caff61ae6d@178.18.253.102:26656,73290354a81324fca070cef5158b272925f102a2@65.109.92.235:11006,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

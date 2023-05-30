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

**live-peers** (12)
```bash
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,7f5ce546e0ffec994995198e0a1b87caff61ae6d@178.18.253.102:26656,5ded92727197e59aa382180628710744910d932b@174.138.23.52:20756,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

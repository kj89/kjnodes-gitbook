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
peers="89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,7f5ce546e0ffec994995198e0a1b87caff61ae6d@178.18.253.102:26656,5ded92727197e59aa382180628710744910d932b@174.138.23.52:20756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

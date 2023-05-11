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

**live-peers** (9)
```bash
peers="03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,73290354a81324fca070cef5158b272925f102a2@65.109.92.235:11006,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,c6e62e0d9998413692ce1aefd05ae5eeb699a691@65.109.122.105:60756,a70d47079283e8bddc0d2c63256b34302f9a0a2b@65.109.65.248:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

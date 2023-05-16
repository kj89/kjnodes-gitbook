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
peers="ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,a70d47079283e8bddc0d2c63256b34302f9a0a2b@65.109.65.248:31656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```

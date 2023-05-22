# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (12)
```bash
peers="57accd1be23702a5b374f84e990d85e4ddac47c8@142.132.237.91:20156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,22b78c53ebc22f9135c22dcecfef5a45df5b49ae@128.140.92.139:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```

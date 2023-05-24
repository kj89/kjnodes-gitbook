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

**live-peers** (11)
```bash
peers="3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,57accd1be23702a5b374f84e990d85e4ddac47c8@142.132.237.91:20156,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,d3ac63ff921486f8aef1eba7870cae1d14c38633@1.15.146.92:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```

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
peers="c06d5254e4ecb69ccae41feff4d75de2dd92154d@149.102.138.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,2285f1aa8784a85081063c1bcafa41bf1bad8f06@95.216.188.182:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,bc8a474a75951713263b2ed96105a70ad38804dc@1.15.131.138:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,39429a15338825ea4fa6b310a7b12505e45b95d0@213.133.100.172:26858"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```

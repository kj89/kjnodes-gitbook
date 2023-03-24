# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (18)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,5e5186020063f7f8a3f3c6c23feca32830a18f33@65.109.174.30:56656,f17030edb4e4ec7143c3e3bbbfaeee3dd1a619f2@194.34.232.224:56656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,e1ca2c14c007cc23e280b191d32b6a3da2389672@65.21.183.66:26656,af5384af4257fdff39a2ee2535a1b74c3e052cad@65.109.229.186:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```

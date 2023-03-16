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

**live-peers** (14)
```bash
peers="0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,19f9022eb4d36164288deec5b0badc1ba2e9a1af@89.163.164.110:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,e2803c99090a9b406c646a3b8ae3dcb8d2dfaf07@65.109.83.24:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,944fd51f8539f77a3d1b2eac781c2f1da62568ca@65.109.70.168:36656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,ae665e6e65b6f9f4496935e52bff733b41214d9a@84.46.247.5:26656,002422812948a68fe851bed557de2d0040d41e06@31.220.80.134:30656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,627d906b9c112752d153e87dfa9925730f6a7414@95.217.105.54:13656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,4ec6f5df28df29e9fad04171a60d6b07a1561914@65.109.71.35:31656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,86cf7d0916950d2b48294ed6106f045a7b25aec7@77.105.137.135:26656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,dd87b06249d7b74030321c020a22e6616af3a8c1@49.13.5.97:26656,19ce67b3c44238b09bebd121ef7341b14a3ff0b9@209.145.62.91:30656,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,4367e2b815008789932148f8af1b720ed7c89d85@84.54.192.204:26656,8185e22360e3d43bd7cb8dc41f402f367285c49e@65.21.3.95:40656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

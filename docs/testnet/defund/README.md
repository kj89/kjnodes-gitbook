# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.5 | **Wasm**: ON

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

**live-peers** (40)
```bash
peers="d941341fa0f985d853f0e044d075234776cf1df6@77.232.37.54:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,ef7aa61f227ae0449f4eda42b00652fe7e1577b1@65.109.85.215:36656,d1b61b43b9475e9d509f720415b75c30cb92bfb3@89.117.58.38:26656,a32570fc38ffbff20cd4cbf72b335f4ef810d017@65.21.105.44:40656,86ba2d9b6d88cd7776147a39b4eb377bd47749fb@62.141.45.243:40656,10c636cde873aa942d1d37c01ec6b91b8231fb43@65.21.57.72:26656,ea1af576f728832d90d4fe9944e45743bb270f24@154.12.245.40:30656,e26206d0e39515fb07915b28e468729340eb112e@38.242.244.163:26656,6f82e772ee8ae1895edc9743dbb269fb7c33f06a@144.91.89.158:30656,38c2e79f4d9043aac5fd699d3bd5b8c3bdab0ab2@154.12.241.185:26656,9f950e7aae61ef055706fc393d62764819d1aa54@62.171.169.230:40656,52a6de973b9ad92caada32c2e65655b4d92578de@65.109.2.29:26656,8db4b24f6d1ad836b8d0ac7222971cd428ff6ca8@185.182.187.136:40656,3db1eb8f5c41b8a551e3edd52e0d6150134d45f4@155.133.22.129:26656,ddde85fd6bbb3db544750411f1bb6d3b5b40e700@65.108.92.199:40656,48fe32b3f93472a26854ee6fef69447f62a265ed@199.175.98.109:26656,2b8a63defdcde856b7c4febac9658ad2ef26befb@65.108.9.230:18656,00d115036d02ca5a5e8498fc1c87d56fd3f7f19c@65.109.106.211:26656,7f8cdf82657d23568c650a87b039539d4b234016@164.68.113.162:30656,78c53aca778b1239158cf4bf6a3aeeb2239501bb@38.242.216.35:40656,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656,ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:61656,e0051024da03786ee8008f2ca310bb3ea05edab1@167.86.102.206:26656,a82e76d4c9e2f3caf5c9b28a7ce48be7374f122d@161.35.90.88:26656,4df8eb475acb402f6c86b710bf1b7ac4fa7a87e9@194.146.13.254:26656,807a0dc497bec0ab730310738ef7d27fd3df7671@155.133.27.248:27656,0f25e490f15bdb3453d2f5a86344d4cd68411233@135.181.88.50:40656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,41c5b53745e065bee2f46970e6590ce1c4884401@164.68.113.190:26656,3209ec925afead6706ac250aae88d1b85a45a2d3@167.86.85.247:30656,28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,2dbf17b447b86f551460a9b131550e9c1aedabfe@89.22.231.244:26656,76d932d75b5de4c1799f8702b0047a4ab3de1b14@154.53.63.156:30656,2687b608599ef656f343a790f21fb3fb9292668e@194.146.13.187:26656,d9516be6f5fffad9d2fa4354126c46ca5a6c9310@154.53.55.128:30656,b8435a6a109a9ad95057ce0f1786caf2e9dd0fcc@93.100.235.162:18656,5a173cbd537b8f75063b2db51131fa906236376e@65.109.93.152:32656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:656,7b93283e8da7a2bf0709ffcb73bfddcc3eaf1f59@144.126.135.89:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (43)
```bash
peers="e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,2a11b3e06f832e430efb41e3c3bb07a42875d20c@154.53.34.112:26657,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,cfddc0756f937110aedf1acaffa4527f549f720d@78.29.44.119:36656,c7f3b61275dc16993c39a1ebc9f6cb5895d11d56@148.251.43.226:15656,780a0beff082046c143a9c110f66078e2154c22c@94.130.137.122:28656,995f13d5d34470bf509a1e35dd748061ec5c1c52@167.86.92.200:26656,10c9aecb4f414d45863cbe1a5f91d04b33fcb638@80.85.242.54:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,073cc8f7e9c414a76d29167a123bc5570cd79c49@217.79.178.127:26656,6e4e946ca9a0f01e6c4123fb49575615a629c90b@65.109.111.159:26656,0caedae543d21fe055dbabc195225b38a48951cd@173.249.0.229:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,139935dfa0a122cfc4a279eef4c5770e278a6196@84.46.246.203:26656,022af16bed61bd5749b989695ccfc3870a2238aa@5.199.139.155:39656,9e05e4a15d6077088cbd84fa5a4311e71556e67a@62.141.37.231:26656,a71be69ab3cae88b9100cc357163e003b11291d1@155.133.22.116:26656,694ef36622642377aec8847df309d1dec708cb28@195.201.197.4:38656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,63f0d4438ebfa588c1879dafcd7f4598dd5f9f19@195.2.80.83:26656,d40bd2a7a5d3dc525e66be78a2bdaf1ff0bc1957@95.214.55.25:29656,c37b742c89a3da2031756416e6fcf565890e47cc@95.216.194.237:26656,a4a0b5b90dbcc92006e7d05d7f6521f120520116@34.75.178.18:26656,61a57359bb79726a93b68b6e748b237731ec30cb@95.216.152.117:39656,32c587c3d9329e6c13c5cd7797eb46b30b628bca@91.107.132.237:26656,a08c70c668256d1e8226e5d62d8fc68b12ec8456@217.76.49.112:26656,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,1b12ae671aae37317b160de81ed2ec10d175910c@154.53.43.67:26656,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,df400991447800ca2de270b1ca402d027dab0378@89.163.220.101:26656,3030536f218c76eb43d05035ac64dda277cdc14d@109.172.45.7:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```

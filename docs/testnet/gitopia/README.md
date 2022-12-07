# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,980e2ec8f4ddba44e4a928452e49f3cae722fce3@65.21.182.244:27656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,b19cf9ffb92876b32e18a97d092e08565e40899b@185.216.203.66:41656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,e8799d0034f6b99cc01916639dc424c7d2548784@185.169.252.60:36656,42ba206efd9dd10847fa20f09a74fde6706442aa@194.146.13.128:60956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
